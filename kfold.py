from sklearn.model_selection import KFold 
kf = KFold(n_splits=5, shuffle=True,random_state=100) 

for train_index, test_index in kf.split(X):
      print("Train:", train_index, "Validation:",test_index)
      X_new=[]
      Y_new=[]
      X_new1=[]
      Y_new2=[]
      X_train, X_test = X[train_index], X[test_index] 
      y_train, y_test = Y[train_index], Y[test_index]
      for i in train_index:
        X_new.append(X[i])
        Y_new.append(Y[i])
      for i in test_index:
        X_new1.append(X[i])
        Y_new2.append(Y[i])
      lm=linear_model.LinearRegression()
      lm.fit(X_new,Y_new)
      preds=lm.predict(X_new)
      sc=r2_score(Y_new,preds)
      print(sc)
      print(lm.coef_,lm.intercept_)
