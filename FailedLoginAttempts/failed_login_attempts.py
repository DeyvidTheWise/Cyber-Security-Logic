import numpy as np
import matplotlib.pyplot as plt

def fuzzy_low_risk(x):
    return np.maximum(0, np.minimum(1, (10 - x) / 10))

def fuzzy_medium_risk(x):
    return np.maximum(0, np.minimum(1, (x - 5) / 5)) * np.maximum(0, np.minimum(1, (20 - x) / 5))

def fuzzy_high_risk(x):
    return np.maximum(0, np.minimum(1, (x - 15) / 5))

def plot_failed_logins():
    x = np.linspace(0, 25, 100)
    low_risk = fuzzy_low_risk(x)
    medium_risk = fuzzy_medium_risk(x)
    high_risk = fuzzy_high_risk(x)

    plt.plot(x, low_risk, label="Low risk", color="green")
    plt.plot(x, medium_risk, label="Medium risk", color="yellow")
    plt.plot(x, high_risk, label="High risk", color="red")
    plt.xlabel("Failed logins")
    plt.ylabel("Membership")
    plt.title("Fuzzy set for failed login attempts")
    plt.legend()
    plt.show()

failed_logins = 10
plot_failed_logins(failed_logins)
