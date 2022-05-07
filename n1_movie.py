"""0. Estabelecer 3 questões de pesquisa sobre os dados
1. Carregar Dados
2. Explorar dados
3. Responder questões de pesquisa
4. Responder questões gráficamente
Release_Date,Title,Overview,Popularity,Vote_Count,
Vote_Average,Original_Language,Genre,Poster_Url								"""

""" Questoes de pesquisa:
    1 - Qual a nota do filme?
    2 - Qual o genero?
    3 - Qual a data de lancamento?"""

import matplotlib.pyplot as plt

def searchData(file, movie):
    for line in file:
        dado = line.split(";")
        if (dado[1] == movie):
            release_date = dado[0]
            vote_avg = dado[5] 
            genre = dado[7]
            file.seek(0)
            return release_date, vote_avg, genre

def graph(movies, vote_avg):
    fig, ax = plt.subplots()
    ax.bar(movies, vote_avg, color="red")
    ax.set_title("Nota IMDB de cada filme")
    ax.set_xlabel("Filmes")
    ax.set_ylabel("Notas")
    fig.savefig("grafico_filmes.pdf")

file = open("mymoviedb.csv", "r", encoding="utf-8")
movies = ["Eternals","The Batman","No Exit","Kimi","Scream","The Hunting"]
vote_avg = []

for i in range(len(movies)):
    release_date, vote, genre = searchData(file, movies[i])
    vote_avg.append(float(vote))
    print(f'Filme: {movies[i]}\n'
          f'Nota: {vote_avg[i]}\n'
          f'Genero: {genre}\n'
          f'Data de lancamento: {release_date}')
    print('-------------------------------------')

graph(movies, vote_avg)
file.close()