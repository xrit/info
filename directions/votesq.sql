select * from polls_choice c join polls_question q on (q.id = c.question_id)
order by c.question_id, c.id;

select sum(c.votes), q.id, q.question_text 
from polls_choice c join polls_question q on (q.id = c.question_id) 
group by q.id, q.question_text
order by sum(c.votes);

