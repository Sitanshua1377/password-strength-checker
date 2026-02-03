import matplotlib.pyplot as plt

def show_meter(score):
    labels = ['Weak', 'Medium', 'Strong']
    values = [score, 7-score, 0]

    plt.bar(labels, [score, 7-score, 0])
    plt.title("Password Strength Meter")
    plt.ylabel("Score")
    plt.show()
