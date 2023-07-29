from EMGdataProcess import load_dataset
from sklearn import preprocessing

train_set_file = 'trainset_P135_60.xls'

validate_set_file = 'cvset_P12345_20.xls'

test_set_file = 'testset_P12345_20.xls'

NC = 8

X_train, Y_train, X_validate, Y_validate, X_test, Y_test = load_dataset(train_set_file, validate_set_file , test_set_file, NC )



# flag_scaling = True
#
# if (flag_scaling):
#     X_train = preprocessing.scale(X_train, axis = 0)
#     X_validate= preprocessing.scale(X_validate, axis = 0)
#     X_test = preprocessing.scale(X_test, axis = 0)
#
#     print('Feature normalization done!')

print(X_train.shape)
print(Y_train.shape)

print(X_test.shape)
print(Y_test.shape)

print(X_validate.shape)
print(Y_validate.shape)
