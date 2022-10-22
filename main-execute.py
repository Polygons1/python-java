import javagen

javagen.start()
javagen.check_jdk()

fn = input("filename (without .java): ")
print(u"\u2193 type print")
wtd = input("(in main) what to do? ")
if wtd == "print":
	whatprint = input("what to print? ")
	action = f'System.out.println("{whatprint}")'
javagen.run_jar(javagen.compile(javagen.generate_file(fn, action)))
