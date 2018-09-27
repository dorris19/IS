lex(triangle, factBase).
lex(angle, subject).
lex(third, descriptor).

lex(the, lang).
lex(is, lang).
lex(a, lang).
lex(of, lang).
lex(is, affirm).
lex(that, lang).
lex(isnt, disprove).
lex(sideangle, theorem).
lex(prove, impWord).
lex(that, affirm).

lex(mathStuff, fact).


:- op(700, xfx, --->).


s		---> [v_IMP, v_CLAIM].
v_IMP		---> [impWord, lang].
v_CLAIM		---> [v_TARGET, v_GOAL].
v_CLAIM		---> [v_GOAL, indicator].
v_GOAL		---> [theorem].
v_GOAL		---> [affirm, fact].
v_GOAL		---> [disprove, fact].
v_TARGET	---> [v_SUBOBJECT, v_OBJECT].
v_SUBOBJECT 	---> [descriptor, subject].
v_SUBOBJECT	---> [lang, descriptor, subject].
v_SUBOBJECT 	---> [subject].
v_OBJECT	---> [lang, factBase].
lang		---> [lang, lang].





%%% Chooses a rule with 'category' on the left hand side. Checks
%%% whether the right hand side can be expanded to match what comes
%%% next in the input string.

%%% Category can be expanded by a lexical rule.
recognize_topdown(Category,[Word|Reststring],Reststring) :-
	/*** Uncomment the following lines to see the steps the top
             down parser takes ***/
	%%% nl, write('String to recognize: '), write([Word|Reststring]), 
	%%% nl, write('Category to recognize: '), write(Category),
	lex(Word,Category).

%%% Category can be expanded by a phrase structure rule.
recognize_topdown(Category,String,Reststring) :-
        Category ---> RHS,
	/*** Uncomment the following lines to see which steps the
             recognizer takes. ***/
        %%% nl, write('Rule: '), write((Category ---> RHS)),
        matches(RHS,String,Reststring).


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% matches(+symbols, +sentence, ?rest of sentence)
%%% Checks whether the list of symbols can be expanded into terminal
%%% symbols that match whats next on the input string.

%%% The list of symbols is empty. -> Return the string unchanged.
matches([],String,String).

%%% The list of symbols was produced by a phrase structure rule and
%%% therefore contains category symbols. Try to recognize a substring
%%% matching the first category on the list, then try to match the
%%% rest of the categories.
matches([Category|Categories],String,RestString) :-
        recognize_topdown(Category,String,String1),
        matches(Categories,String1,RestString).


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% recognize_topdown(+list)
%%% Driver predicate to initialize the category we are looking for
%%% and the difference list. Calls the main predicate
%%% recognize_topdown/3. 

recognize_topdown(String) :-
        recognize_topdown(s,String,[]).
