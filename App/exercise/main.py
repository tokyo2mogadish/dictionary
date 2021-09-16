import justpy as jp

@jp.SetRoute('/home')
def home():#request handler
    wp = jp.WebPage()
    div = jp.Div(a = wp, classes = 'bg-gray-200 h-screen')

    div1 = jp.Div(a = div, classes = 'grid grid-cols-3 gap-4 p-4')#p padding
    in1 = jp.Input(a = div1, placeholder = 'Enter first value',
            classes = 'form-input')
    
    in2 = jp.Input(a = div1, placeholder = 'Enter second value',
            classes = 'form-input')
    #tailwind
    d_output = jp.Div(a = div1, text = 'Result goes here..', classes = 'text-gray-600')
    jp.Div(a = div1, text = 'Just another div..', classes = 'text-gray-600')
    jp.Div(a = div1, text = 'Yet another div..', classes = 'text-gray-600')

    div2 = jp.Div(a = div, classes = 'grid grid-cols-2 gap-4')
    jp.Button(a = div2, text = 'Calculate', click = sum_up, in1 = in1, in2 = in2, d_output = d_output,
            classes = 'border border-blue-500 m-2 py-1 px-4 rounded text-blue-600 hover:bg-red-500 hover:text-white')
    jp.Div(a = div2, text = 'I am cool interactive div.',mouseenter = mouse_enter, mouseleave = mouse_leave,
            classes = 'hover:bg-red-500 hover:text-white hover:font-bold')

    return wp

#event handler
def sum_up(widget, msg):
    suma = float(widget.in1.value) + float(widget.in2.value)
    widget.d_output.text = str(suma)

#event handler
def mouse_enter(widget, msg):
    widget.text = 'Mis je dosao.'

#event handler
def mouse_leave(widget, msg):
    widget.text = 'Otisao je mis.'

jp.justpy()
