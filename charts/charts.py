import matplotlib.pyplot as pylot

def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [200, 34, 120]

    fig, aux = pylot.subplots()
    aux.pie(values, labels=labels)
    pylot.savefig('pie.png')
    pylot.close()