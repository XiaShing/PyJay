import os, sys, subprocess, urllib2

#def install_blog():

#def post():		
	#if (file2.readline() == "<div class=\"blog_menu\">"): #finding current post here.
	#	print "We\'re in!3"
	#	file.write("test")

def main():
	blog = sys.argv[1]
	action = sys.argv[2]
	good_input = 0

	if ((action != "install") and (action != "post")):
		print "action needs to be \'install\' or \'post\'" #Have a menu action as well for unsure people...

	else:
		print action + "ing..."
		file = open(blog,"r+") #We need to open the file regardless of installation, posting, or editting
		
		if (action == "install"): #Need's to 'touch' the file first, otherwise this action results in error.
			print "Blog will be installed as: " + blog
			print "PHP installed? (Y/N)"
			php_choice = raw_input("=> ")

			while (good_input != 1):
				if ((php_choice == "y") or (php_choice == "Y")):
					file.write('<?php echo \"<?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\"?>\"; ?>\n')
					good_input = 1
				elif ((php_choice == "n") or (php_choice == "N")):
					file.write('<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n')
					good_input = 1
				else:
					print "Proper input is needed"
					php_choice = raw_input("=> ")
					good_input = 0
					
			file.write('<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\"\n') #DTD stuff
			file.write(" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">\n")
			file.write("<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"en\" lang=\"en\">\n")
			file.write("\t<head>\n")
			
			print "Enter your blog\'s name"
			blog_name = raw_input("=> ")
			file.write("\t\t<title>" + blog_name + "</title>\n")
			file.write("<link rel=\"stylesheet\" href=\"/style.css\" type=\"text/css\" />\n")
		
			print "Now we need to know your javascript directory."
			print "Please enter the directory in long format. Dont leave a trailing slash"
			print "Example: /javascript"
			print "Example: /blog/javascript"
			javascript_dir = raw_input("=> ") #Get the user's javascript directory
			file.write("<script type=\"text/javascript\" src=\"" + javascript_dir + "/jquery.js\"></script>\n")
			file.write("<script type=\"text/javascript\">\n")
			file.write("\t\t\t$(document).ready(function(){\n")
			file.write("\t\t\t\t$(\".blog_menu span\").hide();\n")
			file.write("\t\t\t\t$(\".blog_menu a\").click(function(event) {\n")
			file.write("\t\t\t\t\t$(this).toggle() {\n")
			file.write("\t\t\t\t\t\t$(this).css({color: \"#FF0000\"});\n")
			file.write("\t\t\t\t\t\t$(this).next(\"span\").slideToggle(\"fast\");\n")
			file.write("\t\t\t\t\t}\n")
			file.write("\t\t\t\t});\n")
			file.write("\t\t\t});\n")
			file.write("\t\t</script>\n")
			file.write("\t</head>\n")
			
			file.write("\n")
			
			file.write("\t<body>\n")
			file.write("\t\tClick a post to read\n")
			file.write("\t\t<div class=\"blog_menu\">\n")
			file.write("\t\t</div>\n")
			file.write("\t</body>\n")
			file.write("</html>")

			print "Blog installed. Would you like to make the first post?"
			print "Re-run the script with the post action"
			'''first_post = raw_input("=> ")
			good_input = 0
			while (good_input != 1):
				if ((first_post == "y") or (first_post == "Y")):
					post()
					good_input = 1
				elif ((first_post == "n") or (first_post == "N")):
					raise KeyboardInterrupt
					good_input = 1 #Probably never reaches this anyway.
				else:
					print "Proper input is needed"
					first_post = raw_input("=> ")
					good_input = 0'''

			print "For security reasons, you should not keep this script in a web-accessible directory, especially if you have mod_python installed.\n"
			
		'''if (action == "post"):
			while (file.readline() != ""
			file.read()'''
			
			#post()
			#end with a . on an empty line to end the post
		
		#if (action == "edit"):
			#regex for finding previous post here.
		
		file.close()
			
def usage():
	print "General usage: python " + sys.argv[0] + " blog_name.php" + " action"
	print "Installation/Re-install blog: python " + sys.argv[0] + " blog_name.php" + " install"
	print "Post to the blog: python " + sys.argv[0] + " blog_name.php" + " post"
	print "Edit a blog post: python " + sys.argv[0] + " blog_name.php" + " edit"
					
if (__name__ == '__main__'):
	if len(sys.argv) < 2:
		usage()
		sys.exit(1)
	try:
		blog = sys.argv[1]
		action = sys.argv[2]
		main()

	except KeyboardInterrupt:
		print "\n"
		print "Caught SIGINT...exiting"
