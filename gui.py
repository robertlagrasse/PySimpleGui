import PySimpleGUI as psg

# Define some objects to put on the window (labels, buttons, etc.)
# the key is a reference value for any information returned on window.read()
label1 = psg.Text('Label1')
input1 = psg.InputText(tooltip='input1 tool tip', key='input1')
label2 = psg.Text('Label2')
input2 = psg.InputText(tooltip='input2 tool tip', key='input2')
label3 = psg.Text('Label3')
input3 = psg.InputText(tooltip='input3 tool tip', key='input3')
button1 = psg.Button('Button1', key='button1')
button2 = psg.Button('Button2', key='button2')
button3 = psg.Button('Button3', key='button3')

dataList = ['data1', 'data2', 'data3']
listbox = psg.Listbox(values=dataList, key='listbox',
                      enable_events=True, size=[45, 10])

# Making this a picture button
button4 = psg.Button(size=2, image_source='image.png',
                     mouseover_colors='LightBlue2', tooltip='Doot!',
                    key='button4')

currentSelectionlabel = psg.Text('Current Selection', key='csl')

fileBrowseLabel = psg.Text('File Browse')
fileBrowseResult = psg.Input('', key='fileBrowseResult', enable_events=True)
fileBrowseButton = psg.FilesBrowse('File(s)', key='fileBrowseButton', enable_events=True)

folderBrowseResult = psg.Input('', key='folderBrowseResult', enable_events=True)
folderBrowseButton = psg.FolderBrowse('Folder', key='folderBrowseButton', enable_events=True)

popupButton = psg.Button('Popup', key='popupButton')
windowLayout = [[label1, input1, button1],
                [label2, input2, button2],
                [label3, input3, button3],
                [listbox, button4],
                [currentSelectionlabel],
                [fileBrowseButton, fileBrowseResult],
                [folderBrowseButton, folderBrowseResult],
                [popupButton]]

# Instantiate a window. Specify a layout using objects defined above
# Layout is a list of lists. Each list is a row of objects
psg.theme('DarkBlue2')
window = psg.Window('Window Name',
                    layout=windowLayout,
                    font=('Helvetica', 20))

# window.read() returns a tuple, an event and a dictionary if any values changed
# the event name is going to be the key of the button specified above
while True:
    event, values = window.read()
    print("event:", event)
    print(values)
    match event:
        case 'button1':
            print(values['input1'])
        case 'button2':
            print(values['input2'])
        case 'button3':
            print(values['input3'])
        case 'button4':
            print(values['listbox'])
        case 'listbox':
            window['csl'].update(value=values['listbox'][0])
        case 'fileBrowseResult':
            print(values['fileBrowseButton'])
        case 'folderBrowseResult':
            print(values['folderBrowseButton'])
        case 'popupButton':
            psg.popup("Like it is hot", font=("Helvetica",20))
        case psg.WIN_CLOSED:
            break

window.close()
