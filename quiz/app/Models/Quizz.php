<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Quizz extends Model
{
    use HasFactory;
    protected $fillable = ['type', 'temps'];
    protected $table = 'quizz';

    public function questions(){
        return $this->hasMany(Question::class, 'quizz');
    }

    public function equipes(){
        return $this->hasMany(Equipe::class, 'quizz');
    }

}
