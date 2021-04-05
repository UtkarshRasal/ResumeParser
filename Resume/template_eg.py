from docxtpl import DocxTemplate
tpl = DocxTemplate('/home/ebabu/Downloads/SrishtiJain 2021-converted.docx')

context = {
'col_labels' : ['fruit', 'vegetable', 'stone', 'thing'],
'tbl_contents': [
    {'label': 'yellow', 'cols': ['banana', 'capsicum', 'pyrite', 'taxi']},
    {'label': 'red', 'cols': ['apple', 'tomato', 'cinnabar', 'doubledecker']},
    {'label': 'green', 'cols': ['guava', 'cucumber', 'aventurine', 'card']},
    ]
}

tpl.render(context)
tpl.save('generated_doc.docx')