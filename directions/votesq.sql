select * from polls_choice c join polls_question q on (q.id = c.question_id);

select sum(c.votes), q.question_text, q.id 
from polls_choice c join polls_question q on (q.id = c.question_id) 
group by q.question_text;

