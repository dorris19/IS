mortal(X) :- human(X).
fallible(X) :- human(X).
immortal(X) :- god(X).

demigod(X) :- god(X), human(X).

falseIdol(X) :- god(X), fallible(X), not(demigod(X)).


human(joe).
human(hercules).
god(hercules).
god(zeus).

