@extends('base')
@section('content')
<form>
    <div>
        <select name="type" id="">
            <option value="">type</option>
            @foreach($types as $type)
            <option value="{{ $type }}">{{ $type }}</option>
            @endforeach
        </select>
        <input type="text" id="" name="type">
        <label for="temps"></label><br>
    </div>
    <div>
        <table>
            <thead>
                <th>Questions</th>
                <th>Réponse</th>
                <th>Points</th>
            </thead>
            <tbody>
                <tr>
                    <tr>
                        <input type="text" name="question[]" id="">
                    </tr>
                    <tr>
                        <input type="text" name="reponse[]" id="">
                    </tr>
                    <tr>
                        <input type="number" name="points[]" id="">
                    </tr>
                </tr>
            </tbody>
        </table>
    </div>
    <input type="text" id="" name="temps"><br>
</form>
@endsection
@section('js')
<script type="text/javascript">

</script>
@endsection
