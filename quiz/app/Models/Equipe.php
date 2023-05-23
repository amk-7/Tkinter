<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Equipe extends Model
{
    use HasFactory;
    protected $fillable = ['nom', 'score'];

    public function quizz(){
        return $this->belongsTo(Quizz::class, 'id');
    }
}
