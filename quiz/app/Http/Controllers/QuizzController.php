<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Equipe;
use App\Models\Question;
use App\Models\Quizz;



class QuizzController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        //dd(Quizz::all()->first()->questions);
        return view('quizz.index')->with([
            "quizz" => Quizz::all()->first(),
            "questions" => Quizz::all()->first()->questions,
            "equipes" => Equipe::all()->whereIn('nom', ['L1', 'L2']),
        ]);
    }

    /**
     * Show the form for creating a new resource.
     */
    public function create()
    {

    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        Quizz::create($request->all());
    }

    /**
     * Display the specified resource.
     */
    public function show(Quizz $quizz)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(Quizz $quizz)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, Quizz $quizz)
    {
        $quizz = $request->all();
        $quizz->save();
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(Equipe $quizz)
    {
        $quizz->delete();
    }
}
