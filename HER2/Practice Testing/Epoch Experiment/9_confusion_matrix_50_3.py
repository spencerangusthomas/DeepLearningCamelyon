from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_test, np.rint(y_pred)))

cf_50_3 = confusion_matrix(y_test, np.rint(y_pred))
