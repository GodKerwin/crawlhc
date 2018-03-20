class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        print(data['conpany_name'])
        print(data['name'])
        print(data['address'])
        print(data['phone'])
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        fout.write("<tr>")
        fout.write("<th>公司</th>")
        fout.write("<th>联系人</th>")
        fout.write("<th>地址</th>")
        fout.write("<th>电话</th>")
        fout.write("</tr>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['conpany_name'])
            fout.write("<td>%s</td>" % data['name'])
            fout.write("<td>%s</td>" % data['address'])
            fout.write("<td>%s</td>" % data['phone'])
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
