<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use App\Models\Quizz;
use App\Models\Question;
use App\Models\Equipe;

class QuizzSeeder extends Seeder
{
    public function run()
    {
        $quizz = Quizz::create([
            'temps' => 20,
            'type' => ''
        ]);


        $equipes = [
            ['L1', 0,],
            ['L2', 0,],
            ['L3', 0,]
        ];

        foreach($equipes as $e){
            $equipe = new Equipe;
            $equipe->nom = $e[0];
            $equipe->score = $e[1];
            $equipe->quizz = $quizz->id;
            $equipe->save();
        }

        $questions = [
            ['Question 1', 'Réponse 1', 10,],
            ['Question 2', 'Réponse 2', 5,],
            ['Question 3', 'Réponse 3', 8,]
        ];

        foreach($questions as $q){
            $question = new Question;
            $question->question = $q[0];
            $question->reponse = $q[1];
            $question->points = $q[2];
            $question->quizz = $quizz->id;
            $question->save();
        }

    }
}

