import justpy as jp


def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text='Analysis of Course Reviews',
                 classes='text-h3 text-center q-pa-md')
    p1 = jp.QDiv(a=wp, text='These Graphs Represent course analysis')

    return wp


jp.justpy(app)
