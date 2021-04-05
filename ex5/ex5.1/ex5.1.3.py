import sys

stdoutOrigin = sys.stdout
sys.stdout = open('ex5.1.3.html', 'w')

i = 0
k = 0

print("<html><body><table>")

# перечисление
for i in range(1, 11):
    print("<tr>")
    for k in range(1, 11):
        print('<td><a href=http://', i * k, '.ru>', i * k, sep="")
        print('</a></td>')
    print("</tr>")

print("</table></body></html>")

sys.stdout.close()
sys.stdout = stdoutOrigin
