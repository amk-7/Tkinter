<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class EquipeController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        //
    }

    /**
     * Show the form for creating a new resource.
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        Equipe::create($request->all());
    }

    /**
     * Display the specified resource.
     */
    public function show(Equipe $equipe)
    {
        
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(Equipe $equipe)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, Equipe $equipe)
    {
        $equipe = $request->all();
        $equipe->save();
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(Equipe $equipe)
    {
        $equipe->delete();
    }
}
