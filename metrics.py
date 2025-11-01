from sklearn.metrics import accuracy_score, precision_score, f1_score, confusion_matrix

def calc_metrics(y_true, y_pred):
    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    fpr = fp / (fp + tn)
    return {
        "accuracy": round(acc * 100, 2),
        "precision": round(prec * 100, 2),
        "f1_score": round(f1 * 100, 2),
        "fpr": round(fpr * 100, 2),
        "tp": int(tp), "fp": int(fp), "fn": int(fn), "tn": int(tn)
    }
