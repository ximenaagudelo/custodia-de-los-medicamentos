from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/404.html')
def not_found():
    return render_template('404.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/service.html')
def service():
    return render_template('service.html')

@app.route('/blog.html')
def blog():
    return render_template('blog.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/faq.html')
def faq():
    return render_template('faq.html')

@app.route('/feature.html')
def feature():
    return render_template('feature.html')

@app.route('/team.html')
def team():
    return render_template('team.html')

@app.route('/testimonial.html')
def testimonial():
    return render_template('testimonial.html')

if __name__ == '__main__':
    app.run(debug=True)