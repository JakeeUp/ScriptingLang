def make_shirt(size="large",message="I love Python"):
    print(f"making a {size} shirt with the message: {message}")

make_shirt()
#do not have to use size= its automatic due to the default def 
make_shirt("medium")
make_shirt("small" , "Python is amazing")