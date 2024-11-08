import random
import math

from keras.src.ops import switch

def generate_samples(num_samples):
    y = [random.uniform(0, 10) for _ in range(num_samples)]
    y_hat = [random.uniform(0, 10) for _ in range(num_samples)]
    return y, y_hat

def mae(y, y_hat):
    return sum(abs(yi - y_hat_i) for yi, y_hat_i in zip(y, y_hat)) / len(y)

def mse(y, y_hat):
    return sum((yi - y_hat_i) ** 2 for yi, y_hat_i in zip(y, y_hat)) / len(y)

def rmse(y, y_hat):
    return math.sqrt(mse(y, y_hat))

def huber_loss(y, y_hat, delta=0.5):
    loss = 0
    for yi, y_hat_i in zip(y, y_hat):
        diff = abs(yi - y_hat_i)
        if diff <= delta:
            loss += 0.5 * (yi - y_hat_i) ** 2
        else:
            loss += delta * diff - 0.5 * delta ** 2
    return loss / len(y)

def main():
    try:
        num_samples = int(input("Enter the number of samples: "))
        if num_samples <= 0:
            print("number of samples must be a positive integer number")
            return

        loss_name = input("Enter loss function name (MAE, MSE, RMSE, Huber_Loss): ")
        if loss_name not in ["MAE", "MSE", "RMSE", "Huber_Loss"]:
            print(f"loss name {loss_name} is not supported")
            return

        y, y_hat = generate_samples(num_samples)

        if len(y) != num_samples or len(y_hat) != num_samples:
            print("The number of samples is incorrect")
            return

        print("target:", y)
        print("predict:", y_hat)

        if loss_name == "MAE":
            result = mae(y, y_hat)
        elif loss_name == "MSE":
            result = mse(y, y_hat)
        elif loss_name == "RMSE":
            result = rmse(y, y_hat)
        elif loss_name == "Huber_Loss":
            result = huber_loss(y, y_hat)
        print(f"{loss_name}:", result)

    except ValueError:
        print("number of samples must be a positive integer number")

if __name__ == "__main__":
    main()
