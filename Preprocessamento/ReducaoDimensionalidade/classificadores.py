from sklearn.ensemble import RandomForestClassifier
from sklearn.dummy import DummyClassifier
from sklearn.model_selection import train_test_split
from numpy import random

def random_forest_classifica(X, y):
    
    SEED = 123143
    random.seed(SEED)
    
    treino_x, teste_x, treino_y, teste_y = train_test_split(X, 
                                                        y,
                                                        test_size = 0.3)
    classificador = RandomForestClassifier(n_estimators = 100)
    classificador.fit(treino_x, treino_y)

    return f"Resultado da classificação RAND FOREST: {classificador.score(teste_x,teste_y)*100:.6f}"

def dummy_classifica(X, y):
    
    SEED = 123143
    random.seed(SEED)
    
    treino_x, teste_x, treino_y, teste_y = train_test_split(X, 
                                                        y,
                                                        test_size = 0.3)

    classificador = DummyClassifier(strategy="most_frequent")
    classificador.fit(treino_x, treino_y)
    
    return f"Resultado da classificação DUMMY: {classificador.score(teste_x,teste_y)*100:.6f}"