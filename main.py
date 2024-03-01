from pytube import YouTube
import os
from flask import Flask,render_template,request
def Download(link, output_path):
    try:
        yt = YouTube(link)
        
        # Get the highest resolution stream
        yt_stream = yt.streams.filter(file_extension='mp4').get_highest_resolution()

        download_path = os.path.join(output_path)
        if not os.path.exists(download_path):
            os.makedirs(download_path)

        yt_stream.download(output_path=download_path)
        return 'Download successful!'
    except Exception as e:
        return f'An error occurred: {str(e)}'

'''def Search(Term):
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.youtube.com/")
        search_box = driver.find_element("name", "search_query")
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
        driver.implicitly_wait(5)
        video=driver.find_element_by_id("video-title").get_attribute("href")
        Download(video,output_path='.')
    except Exception as e:
        return f'An error occured: {e}'''

app=Flask(__name__)
Port=3011

@app.route("/",methods=['GET','POST'])

def startpy():
    return render_template('index.html')
    
@app.route('/download', methods=['GET','POST'])
def process():
    link = request.form['linkbox']
    path=request.form['path']
    #search = request.form['search']
    if link:

        result=Download(link,path)
    '''else:
        result=Search(search)'''
    return render_template('download.html',result=result)

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=Port)