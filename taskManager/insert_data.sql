-- Supprimer les utilisateurs existants (si nécessaire)
DELETE FROM auth_user;

-- Insérer des utilisateurs
INSERT INTO auth_user (password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined)
VALUES 
('pbkdf2_sha256$260000$A1B2C3D4$E5F6G7H8I9J0K1L2M3N4', CURRENT_TIMESTAMP, true, 'admin', '', '', 'admin@example.com', true, true, CURRENT_TIMESTAMP),
('pbkdf2_sha256$260000$A1B2C3D4$E5F6G7H8I9J0K1L2M3N4', CURRENT_TIMESTAMP, false, 'ayeda', '', '', 'ayeda@example.com', false, true, CURRENT_TIMESTAMP),
('pbkdf2_sha256$260000$A1B2C3D4$E5F6G7H8I9J0K1L2M3N4', CURRENT_TIMESTAMP, false, 'user1', '', '', 'user1@example.com', false, true, CURRENT_TIMESTAMP),
('pbkdf2_sha256$260000$A1B2C3D4$E5F6G7H8I9J0K1L2M3N4', CURRENT_TIMESTAMP, false, 'user2', '', '', 'user2@example.com', false, true, CURRENT_TIMESTAMP),
('pbkdf2_sha256$260000$A1B2C3D4$E5F6G7H8I9J0K1L2M3N4', CURRENT_TIMESTAMP, false, 'user3', '', '', 'user3@example.com', false, true, CURRENT_TIMESTAMP);

-- Supprimer les groupes existants (si nécessaire)
DELETE FROM tasks_group;

-- Insérer des groupes
INSERT INTO tasks_group (name, leader_id)
VALUES 
('Development Team', (SELECT id FROM auth_user WHERE username='ayeda')),
('Marketing Team', (SELECT id FROM auth_user WHERE username='admin')),
('Support Team', (SELECT id FROM auth_user WHERE username='user1')),
('Sales Team', (SELECT id FROM auth_user WHERE username='user2')),
('HR Team', (SELECT id FROM auth_user WHERE username='user3'));

-- Supprimer les membres de groupes existants (si nécessaire)
DELETE FROM tasks_groupmembership;

-- Insérer des membres dans les groupes
INSERT INTO tasks_groupmembership (group_id, user_id)
VALUES 
((SELECT id FROM tasks_group WHERE name='Development Team'), (SELECT id FROM auth_user WHERE username='admin')),
((SELECT id FROM tasks_group WHERE name='Development Team'), (SELECT id FROM auth_user WHERE username='user1')),
((SELECT id FROM tasks_group WHERE name='Marketing Team'), (SELECT id FROM auth_user WHERE username='ayeda')),
((SELECT id FROM tasks_group WHERE name='Support Team'), (SELECT id FROM auth_user WHERE username='user2')),
((SELECT id FROM tasks_group WHERE name='Sales Team'), (SELECT id FROM auth_user WHERE username='user3'));

-- Supprimer les tâches existantes (si nécessaire)
DELETE FROM tasks_task;

-- Insérer des tâches
INSERT INTO tasks_task (title, description, due_date, priority, status, created_by_id, assigned_to_id, progress, updated_at)
VALUES 
('First Task', 'This is the first task', '2024-12-31', 'Medium', 'Pending', (SELECT id FROM auth_user WHERE username='ayeda'), (SELECT id FROM auth_user WHERE username='admin'), 0, CURRENT_TIMESTAMP),
('Second Task', 'This is the second task', '2024-11-30', 'High', 'In Progress', (SELECT id FROM auth_user WHERE username='admin'), (SELECT id FROM auth_user WHERE username='ayeda'), 50, CURRENT_TIMESTAMP),
('Third Task', 'This is the third task', '2024-10-31', 'Low', 'Completed', (SELECT id FROM auth_user WHERE username='user1'), (SELECT id FROM auth_user WHERE username='user2'), 100, CURRENT_TIMESTAMP),
('Fourth Task', 'This is the fourth task', '2024-09-30', 'High', 'Pending', (SELECT id FROM auth_user WHERE username='user2'), (SELECT id FROM auth_user WHERE username='user3'), 0, CURRENT_TIMESTAMP),
('Fifth Task', 'This is the fifth task', '2024-08-31', 'Medium', 'In Progress', (SELECT id FROM auth_user WHERE username='user3'), (SELECT id FROM auth_user WHERE username='user1'), 25, CURRENT_TIMESTAMP);

-- Supprimer les commentaires existants (si nécessaire)
DELETE FROM tasks_comment;

-- Insérer des commentaires
INSERT INTO tasks_comment (task_id, content, created_at, created_by_id)
VALUES 
((SELECT id FROM tasks_task WHERE title='First Task'), 'This is a comment on the first task', CURRENT_TIMESTAMP, (SELECT id FROM auth_user WHERE username='admin')),
((SELECT id FROM tasks_task WHERE title='Second Task'), 'This is a comment on the second task', CURRENT_TIMESTAMP, (SELECT id FROM auth_user WHERE username='ayeda')),
((SELECT id FROM tasks_task WHERE title='Third Task'), 'This is a comment on the third task', CURRENT_TIMESTAMP, (SELECT id FROM auth_user WHERE username='user1')),
((SELECT id FROM tasks_task WHERE title='Fourth Task'), 'This is a comment on the fourth task', CURRENT_TIMESTAMP, (SELECT id FROM auth_user WHERE username='user2')),
((SELECT id FROM tasks_task WHERE title='Fifth Task'), 'This is a comment on the fifth task', CURRENT_TIMESTAMP, (SELECT id FROM auth_user WHERE username='user3'));
