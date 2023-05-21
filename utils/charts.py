import matplotlib.pyplot as ptl

def show_bar_chart(labels, values):
    fig, ax = ptl.subplots()
    ax.bar(labels, values)
    ptl.show()

def show_plot_chart(labels, values, country_name):
    fig, ax = ptl.subplots()
    ax.plot(labels, values, marker='o', color='b', linestyle='--', label='Population')
    ax.set(xlabel="Years", ylabel="Population", title=f"{country_name} Population")
    ax.legend()
    ptl.show()

def show_pie_chart(labels, values):
    fig, ax = ptl.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%')
    ptl.show()