-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
WITH TeacherGradedAssignments AS (
    SELECT 
        teacher_id,
        COUNT(*) AS total_assignments
    FROM 
        assignments
    WHERE 
        grade IS NOT NULL
    GROUP BY 
        teacher_id
),
TopTeacher AS (
    SELECT 
        teacher_id
    FROM 
        TeacherGradedAssignments
    ORDER BY 
        total_assignments DESC
    LIMIT 1
)
SELECT 
    COUNT(*) AS grade_a_count
FROM 
    assignments
WHERE 
    teacher_id = (SELECT teacher_id FROM TopTeacher)
    AND grade = 'A';
