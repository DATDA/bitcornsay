import sys

if len(sys.argv)==1:
    message = "Bitcorn Charles The Night Terror says hello"
else:
    message = sys.argv[1]
tmp = sys.stdin.readlines()[0]
if(len(tmp)>0):
    message = tmp


print"                  /"
print"          |\    // "
print"         _| \-///"
print"        /      \\"
print"     *//    0 0 \\                  "
print"    *//         |           %s        " % message
print"   *//    \      \\                 "
print"  *|||     | .  .|                  "
print" *///     / \###/"
print"             ```"

#
