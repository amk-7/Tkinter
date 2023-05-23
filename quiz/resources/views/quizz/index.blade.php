@extends('layout.base')

@section('content')
    <div class="container">
        <div class="row">
            <div class="col-md-6">
                <h1>Quizz : {{ $quizz->type }} Temps : <span id="tempsRestant">{{ $quizz->temps }}s</span></h1>
                <h3>Question : <span id="question"></span> | Points : <span id="points"></span></h3>
                <table class="table" border="1">
                    <thead>
                        <tr>
                            <th>Equipe</th>
                            <th>{{ $equipes[0]->nom }}</th>
                            <th>{{ $equipes[1]->nom }}</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Points</td>
                            <td id="equipe1Points">0</td>
                            <td id="equipe2Points">0</td>
                        </tr>
                        <tr>
                            <td></td>
                            <td>
                                <button class="btn btn-success" id="equipe1WinBtn">Win</button>
                            </td>
                            <td>
                                <button class="btn btn-success" id="equipe2WinBtn">Win</button>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
@endsection

@section('js')
    <script type="text/javascript">
        document.addEventListener('DOMContentLoaded', function() {
            // Récupérer les questions depuis l'attribut data-question
            var questions = @json($questions);
            var tempsQuizz = {{ $quizz->temps }};
            var tempsRestant = tempsQuizz;

            // Fonction pour afficher une question et ses points
            function afficherQuestion(question, points) {
                document.getElementById('question').textContent = question;
                document.getElementById('points').textContent = points;
                tempsRestant = tempsQuizz; // Réinitialiser le temps restant à chaque nouvelle question
                afficherTempsRestant();
                // Relancer le décompte pour la nouvelle question
                clearInterval(intervalId);
                lancerDecompte();
            }

            // Fonction pour afficher le temps restant
            function afficherTempsRestant() {
                document.getElementById('tempsRestant').textContent = tempsRestant + 's';
            }


            // Fonction pour mettre à jour les points d'une équipe
            function mettreAJourPointsEquipe(equipe, points) {
                var equipePointsEl = document.getElementById('equipe' + equipe + 'Points');
                var equipePoints = parseInt(equipePointsEl.textContent);
                equipePoints += points;
                equipePointsEl.textContent = equipePoints;
            }

            // Fonction pour afficher le gagnant
            function afficherGagnant() {
                var equipe1Points = parseInt(document.getElementById('equipe1Points').textContent);
                var equipe2Points = parseInt(document.getElementById('equipe2Points').textContent);

                if (equipe1Points > equipe2Points) {
                    alert("L'équipe 1 a gagné !");
                } else if (equipe2Points > equipe1Points) {
                    alert("L'équipe 2 a gagné !");
                } else {
                    alert("Match nul !");
                    clearInterval(intervalId);
                }
            }

            // Gérer le clic sur le bouton "Win" de l'équipe 1
            document.getElementById('equipe1WinBtn').addEventListener('click', function() {
                var _ = questions[0]; // Prendre la première question et la supprimer du tableau
                questions.shift();
                var question = questions[0];
                if (question) {
                    mettreAJourPointsEquipe(1, _.points);
                    afficherQuestion(question.question, question.points);
                } else {
                    mettreAJourPointsEquipe(1, _.points);
                    afficherGagnant();
                }
            });

            // Gérer le clic sur le bouton "Win" de l'équipe 2
            document.getElementById('equipe2WinBtn').addEventListener('click', function() {
                var _ = questions[0]; // Prendre la première question et la supprimer du tableau
                questions.shift();
                var question = questions[0];
                if (question) {
                    mettreAJourPointsEquipe(2, _.points);
                    afficherQuestion(question.question, question.points);
                } else {
                    mettreAJourPointsEquipe(2, _.points);
                    afficherGagnant();
                }
            });

            // Afficher la première question et ses points au chargement de la page
            var premiereQuestion = questions[0];
            if (premiereQuestion) {
                afficherQuestion(premiereQuestion.question, premiereQuestion.points);
            } else {
                afficherGagnant();
            }
            // Fonction pour lancer le décompte
            function lancerDecompte() {
                intervalId = setInterval(function() {
                    tempsRestant--;
                    afficherTempsRestant();

                    if (tempsRestant === 0) {
                        clearInterval(intervalId);
                        passerQuestionSuivante();
                    }
                }, 1000);
            }

            // Fonction pour passer à la question suivante
            function passerQuestionSuivante() {
                var _ = questions[0]; // Prendre la première question et la supprimer du tableau
                questions.shift();
                var question = questions[0];
                if (question) {
                    afficherQuestion(question.question, question.points);
                } else {
                    afficherGagnant();
                }
            }

            // Lancer le décompte initial
            var intervalId;
            // lancerDecompte();
        });
    </script>
@endsection
