from gensim.models import Word2Vec
from gensim.models.word2vec import Text8Corpus

def evaluate_model(model):
    count = 0
    error = 0
    for line in open("./questions-words.txt"):
        if line.split()[0] == ':':
            continue
        w0, w1, w2, w3 = line.lower().split()
        try:
            predict = model.wv.most_similar(positive=[w1, w2],negative=[w0], topn=1)
            error_now = model.wv.distance(w3, predict[0][0])
            if error_now != float('inf'):
                error += error_now 
                count+=1
        except KeyError: 
            continue
        
    mean_error = error/count
    return mean_error

for i in range(24): #vao ser 24 execuções
    alg = input() #cbow = 0, sg = 1
    size = input() #qual vai ser o size da entrada
    window = input() #qual vai ser a janela 

    model = Word2Vec(size = int(size), window = int(window), sg = int(alg)) #deixar o min_count no default -- so pra analise msm
    model.build_vocab(Text8Corpus("filtered.txt"))
    model.train(Text8Corpus("filtered.txt"),epochs=5, total_examples=model.corpus_count)

    params = "Exec: " + str(i) + " Alg: " + alg + " Size: " + size + " Window: " + window
    print(params)
    print("Erro: ", evaluate_model(model))
    print('\n')