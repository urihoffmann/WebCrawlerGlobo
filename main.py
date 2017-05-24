from crawler import Crawler
from flask import Flask, make_response, request, render_template

app = Flask(__name__)

def validate_user(username, password):
    return username == "editoraglobo" and password == "challenge"


@app.route('/')
def api_root():
    return render_template('auth.html')

@app.route('/feed', methods=['POST'])
def api_auth():
    user = request.form.get('username')
    password = request.form.get('password')
    if not validate_user(user, password):
        return make_response("Invalid user/password", 401)

    crawler = Crawler()
    content = crawler.getContent("http://revistaautoesporte.globo.com/rss/ultimas/feed.xml")
    # content = open('test.xml').read()
    # content = BeautifulSoup(content, "lxml-xml")
    parsedContent = make_response(crawler.parseContent(content), 200)
    return parsedContent

if __name__ == '__main__':
    app.run()
