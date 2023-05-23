<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('quizz', function (Blueprint $table) {
            $table->id();
            $table->string('temps')->unsigned;
            $table->enum("type", ["", "", ""]);
            $table->timestamps();
            $table->unique(['type', 'temps']);
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('quizz');
    }
};
