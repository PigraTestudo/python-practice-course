i = 0
k = 0

print("<html><body><table>")

# перечисление
for i in range(1, 11):
    print("<tr>")
    for k in range(1, 11):
        print("<td>")
        print(i * k)
        print("</td>")
    print("</tr>")

print("</table></body></html>")
