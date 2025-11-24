insert into app_user (email, given_name, surname, city, phone_number, profile_description, password)
values 
  ('aliya.alikyzy@care.com',  'Aliya', 'Aliyeva', 'Astana', '+77770000001', 'Experienced babysitter', 'passAliya'),
  ('askar.askuly@member.com','Askar', 'Askarov',  'Astana', '+77770000002', 'Looking for elderly caregiver', 'passAskar'),
  ('amina.kairat@care.com', 'Amina', 'Kairat', 'Almaty', '+77010000001', 'Playmate for children', 'passKai'),
  ('aktoty.bolat@member.com', 'Aktoty', 'Bolat', 'Almaty', '+77011231122', 'Experienced babysitter', 'passAktoty'),
  ('alen.kazhymykan@member.com', 'Alen', 'Kazhymykan', 'Astana', '+77273334455', 'Looking for elderly caregiver', 'passAlen'),
  ('aiym.kossdauletova@member.com', 'Aiym', 'Kossdauletova', 'Aktobe', '+77776676767', 'Playmate for children', 'passAiym'),
  ('bekarys.bekarysylu@care.com', 'Bekarys', 'Bekarysylu', 'Taldykorgan', '+77778886655', 'Experienced babysitter', 'passBekarys'),
  ('zhanar.dugalova@care.com', 'Zhanar', 'Dugalova', 'Almaty', '+77017017777', 'Looking for elderly care', 'passZhanar'),
  ('bayan.maxatkyzy@member.com', 'Bayan', 'Maxatkyzy', 'Astana', '+77777542233', 'Playmate for children', 'passBayan'),
  ('ainur.ainurkyzy@care.com', 'Ainur', 'Ainurkyzy', 'Astana', '+77778889900', 'Experienced babysitter', 'passAinur'),
  ('arman.armanov@care.com', 'Arman', 'Armanov', 'Almaty', '+77011700000', 'Looking for elderly care', 'passArman'),
  ('daniel.kassym@care.com', 'Daniel','Kassym','Astana', '+77015553322', 'Reliable caregiver with 3 years experience', 'passDan'),
  ('madina.ashim@member.com','Madina', 'Ashim', 'Shymkent','+77012220011', 'Mother of two seeking help', 'passMad'),
  ('yerlan.bolat@care.com', 'Yerlan', 'Bolat', 'Almaty', '+77017770022', 'Energetic playmate', 'passYer'),
  ('dariya.saparova@care.com', 'Dariya', 'Saparova', 'Astana', '+77013334444', 'Certified babysitter with first aid skills', 'passDar'),
  ('kairat.nurgali@member.com', 'Kairat', 'Nurgali', 'Karaganda', '+77778887766', 'Looking for elderly caretaker for father', 'passKai'),
  ('meruyert.kadyrova@care.com', 'Meruyert','Kadyrova', 'Astana', '+77019998811', 'Babysitter and playmate', 'passMeru'),
  ('serik.sarsen@member.com', 'Serik', 'Sarsen', 'Almaty', '+77014445566', 'Searching for playmate for daughter', 'passSer'),
  ('aigerim.tursyn@member.com', 'Aigerim', 'Tursyn', 'Astana', '+77016667788', 'Needs elderly care for grandmother', 'passAig'),
  ('dias.omarov@care.com', 'Dias', 'Omarov', 'Shymkent', '+77011112233', 'Strong and patient elderly care worker', 'passDias'),
  ('amina.aminova@member.com', 'Amina', 'Aminova', 'Astana', '+77770001122', 'Family with 3-year-old looking for help', 'passAmina');

insert into caregiver (caregiver_user_id, photo, gender, caregiving_type, hourly_rate)
values 
  (1, 'aliya.jpg', 'F', 'babysitter', 9.50),
  (3, 'amina.jpg', 'F', 'playmate for children', 7),
  (7, 'bekarys.jpg', 'M', 'babysitter', 8.5),
  (8, 'zhanar.jpg', 'F', 'caregiver for elderly', 8),
  (10, 'ainur.jpg', 'M', 'babysitter', 7.5),
  (11, 'arman.jpg', 'M', 'caregiver for elderly', 9),
  (12, 'daniel.jpg',  'M', 'caregiver for elderly', 10.00),
  (14, 'yerlan.jpg',  'M', 'playmate for children',  8.00),
  (15, 'dariya.jpg',  'F', 'babysitter',            11.00),
  (20, 'dias.jpg',    'M', 'caregiver for elderly', 10.50);

insert into member (member_user_id, house_rules, dependent_description)
values 
  (2, 'No pets. Soft-spoken caregiver preferred.', 'Elderly grandfather with mobility issues'),
  (4, 'Soft spoken babysitter. Active play.', 'child'),
  (5, 'A lot of energy and activitties. More friend type sitter', 'Bored elderly'),
  (6, 'Extraverted. Encouraging conversations', '8 - year old'),
  (9, 'Intellectual. Likes playing chess', '12-year old'),
  (13, 'Flexible schedule, careful with toddlers.', '2-year-old twins'),
  (16, 'No pets. Careful handling, medicine reminders.', 'Father with limited mobility'),
  (18, 'Playmate for daughter, must be patient and kind.', '7-year-old girl, very active'),
  (19, 'Respectful, calm, must understand elderly needs.', 'Grandmother with early dementia'),
  (21, 'Weekend help, gentle play, no screen time.', '3-year-old child who loves stories');

insert into address (member_user_id, house_number, street, town)
values
  (2, 10, 'Kabanbay Batyr', 'Astana'),
  (4, 151, 'Seifullina', 'Almaty'),
  (5, 52, 'Uly Dala', 'Astana'), 
  (6, 24, 'Al-Farabi', 'Aktobe'),
  (9, 78, 'Mangilik el', 'Astana'), 
  (13, 55, 'Shymkent Plaza', 'Shymkent'), 
  (16, 34, 'Dostyk', 'Karagandy'),
  (18, 55, 'Tole bi', 'Almaty'), 
  (19, 66, 'Nuly zhol', 'Astana'), 
  (21, 8, 'Kabanbay Batyr', 'Astana');

insert into job (member_user_id, required_caregiving_type, other_requirements, date_posted)
values 
  (2, 'caregiver_for_elderly', 'Soft-spoken caregiver. No pets.', '2025-11-01'),
  (4, 'child', 'Soft spoken babysitter. Active play.', '2024-11-01'), 
  (5, 'Bored elderly', 'A lot of energy and activitties. More friend type sitter', '2025-06-05'), 
  (6, '8 - year old', 'Extraverted. Encouraging conversations', '2025-03-09'), 
  (9, '12-year old', 'Intellectual. Likes playing chess', '2023-09-09'), 
  (13, '2-year-old twins', 'Flexible schedule, careful with toddlers.', '2024-08-24'), 
  (16, 'Father with limited mobility', 'No pets. Careful handling, medicine reminders.', '2025-03-03'), 
  (18, '7-year-old girl, very active', 'Playmate for daughter, must be patient and kind. Soft-spoken caregiver.', '2024-04-04'), 
  (19, 'Grandmother with early dementia', 'Respectful, calm, must understand elderly needs. No pets', '2025-02-09'), 
  (21, '3-year-old child who loves stories', 'Weekend help, gentle play, no screen time.', '2024-07-09');

insert into job_application(caregiver_user_id, job_id, date_applied)
values 
  (1, 1, '2025-11-02'),
  (3, 1, '2025-11-03'),
  (7, 1, '2025-11-04'),
  (8, 2, '2024-11-03'),
  (10, 2, '2024-11-04'),
  (11, 3, '2025-06-06'),
  (12, 4, '2025-03-10'),
  (14, 5, '2023-09-10'),
  (15, 6, '2024-08-25'),
  (20, 7, '2025-03-04');

insert into appointment ( caregiver_user_id, member_user_id, appointment_date, appointment_time, work_hours, status)
values 
  (1, 2,  '2025-11-10', '09:00', 3, 'accepted'),
  (3, 2,  '2025-11-12', '14:00', 2, 'accepted'),
  (7, 4,  '2025-11-15', '10:30', 4, 'pending'),
  (8, 5,  '2025-11-18', '16:00', 3, 'accepted'),
  (10, 6, '2025-11-20', '11:00', 5, 'declined'),
  (11, 9, '2025-11-22', '09:30', 2, 'accepted'),
  (12, 13,'2025-11-25', '13:00', 6, 'accepted'),
  (14, 16,'2025-11-27', '15:00', 3, 'pending'),
  (15, 18,'2025-11-29', '18:00', 4, 'accepted'),
  (20, 19,'2025-12-01', '08:00', 5, 'accepted');

