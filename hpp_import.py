import sublime, sublime_plugin

def removeComments(line):
	if line.count("//") != 0:
		pos = line.find("//")
		line = line[0:pos]
	return line

class HppImportCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		#self.view.insert(edit, 0, "Hello, World!")
		# Retrieve current .cpp file name and build .hpp file name.
		cPath = self.view.file_name()
		hPath = cPath[:-3] + "hpp"
		sublime.status_message("Looking up " + hPath)

		try:
			hFile = open(hPath, 'r')
		except IOError:
			sublime.status_message("Couldn't open " + hPath + ". Is this file in the same folder?")

		with hFile:
			classFound = False
			for line in hFile:
				# If line starts with "class", process it.
				if line.startswith("class"):
					# Extract class name (second word in the line).
					className = line.split(' ')[1]
					# It could be a forward declaration, in which case, not interested.
					if className.count(";") == 0:
						classFound = True
						break

			if classFound:
				className = className.strip(" \t\n")
				pos = self.view.sel()[0].begin()
				(r,c) = self.view.rowcol(pos)

				# Get hpp file name, include it at top of cpp file + line breaks
				hPathRel = hPath.split("\\")[-1].strip(" \t\n")
				self.view.insert(edit, pos, "#include \"" + hPathRel + "\"\n\n")
				# Move to next lines
				r += 2
				pos = self.view.text_point(r,c)

				# Read lines until we get the closing curly bracket.
				# Curly brackets may be used by other blocks than the class declaration but WHO CAREZ
				for line in hFile:
					if line.count("}") != 0:
						break

					line = removeComments(line)
					line = line.strip(" \t\n")

					# Lines ending with ");" are probably functions
					if line.endswith(");"):
						# Strip that ";"
						line = line[:-1]
						# Special processing for static methods
						if line.startswith("static "):
							# Skip the static at the beginning of the line
							line = line[7:]
						# Special processing for constructors and destructrors
						if line.startswith(className + "(") or line.startswith("~"):
							line = className + "::" + line
						# Normal processing
						else:
							rType = line.split(" ")[0]
							line = rType + " " + className + "::" + line[len(rType)+1:]
						# Add curly braces and line breaks to the line string
						line = line + "\n{\n\t\n}\n"
						self.view.insert(edit, pos, line + "\n")
						# Move to next lines
						r += 5
						pos = self.view.text_point(r,c)

				sublime.status_message("Imported " + className + " methods from " + hPathRel + ".")
