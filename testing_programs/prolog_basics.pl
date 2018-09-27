%Really basic rules and if statement
mortal(X) :- human(X).
fallible(X) :- human(X).
immortal(X) :- god(X).

demigod(X) :- god(X), human(X).

%not means not
falseIdol(X) :- god(X), fallible(X), not(demigod(X)).


human(joe).
human(hercules).
god(hercules).
god(zeus).

%CFG things

%Declaration of ---> operator
:- op(700, xfx, --->).

s     ---> [np,vp].
np    ---> [pn].
np    ---> [pn,rel].
np    ---> [det, nbar].
nbar  ---> [n].
nbar  ---> [n,rel].
rel   ---> [wh,vp].
vp    ---> [iv].
vp    ---> [tv,np].
vp    ---> [dv,np,pp].
vp    ---> [sv,s].
pp    ---> [p,np].

%Assigns a word to a part of grammar

lex(vincent,pn).
lex(mia,pn).
lex(marsellus,pn).
lex(jules,pn).
lex(a,det).
lex(the,det).
lex(her,det).
lex(his,det).
lex(gun,n).
lex(robber,n).
lex(man,n).
lex(woman,n).
lex(who,wh).
lex(that,wh).
lex(to,p).
lex(died,iv).
lex(fell,iv).
lex(loved,tv).
lex(shot,tv).
lex(knew,tv).
lex(gave,dv).
lex(handed,dv).
lex(knew,sv).
lex(believed,sv).

%Definition which determines if a given input is a sentence work right to left in grammar rules

recognize_bottomup([s]).

recognize_bottomup(String) :-
	split(String, Front, Middle, Back),
	( Cat ---> Middle
	 ;
	  (Middle = [Word], lex(Word, Cat))
	),
	append(Front,[Cat|Back],NewString),
	recognize_bottomup(NewString).

split(ABC, A, B, C) :-
	append(A, BC, ABC),
	append(B, C, BC).

%Now we will use a definition from left to right

%%% recognize_topdown(category,+sentence,?rest of sentence)
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
