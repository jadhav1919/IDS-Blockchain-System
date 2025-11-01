from metrics import calc_metrics
y_true = [0, 0, 1, 1, 1, 0]
y_pred = [0, 1, 1, 1, 0, 0]
print(calc_metrics(y_true, y_pred))
