from subprocess import call
print("---------------------")
print("ciao ciao")
call(["docker","run --rm -it -p 9595:8888 -v \"$(pwd):/notebooks\" docker-td"])
