create table app_user (
    user_id serial primary key,
    email varchar (250) not null unique,
    given_name varchar (100) not null, 
    surname varchar (100) not null,
    city varchar (50) not null, 
    phone_number varchar(30) not null,
    profile_description text, 
    password varchar(50) not null
);

create table caregiver (
    caregiver_user_id integer primary key, 
    photo varchar (250), 
    gender varchar (10), 
    caregiving_type varchar (50) not null, 
    hourly_rate numeric not null check (hourly_rate >= 0),

    constraint caregiver_const
    foreign key (caregiver_user_id)
    references app_user (user_id)
    on delete cascade
);

create table member(
    member_user_id integer primary key, 
    house_rules text, 
    dependent_description text,

    constraint member_const
    foreign key (member_user_id)
    references app_user (user_id)
    on delete cascade
);

create table address(
    member_user_id integer primary key,
    house_number numeric, 
    street varchar(100), 
    town varchar(100),

    constraint address_const
    foreign key (member_user_id)
    references member(member_user_id)
    on delete cascade
);

create table job(
    job_id serial primary key, 
    member_user_id integer not null, 
    required_caregiving_type varchar(100) not null, 
    other_requirements text,
    date_posted date not null default current_date,

    constraint job_const
    foreign key (member_user_id)
    references member(member_user_id)
    on delete cascade
);

create table job_application(
    caregiver_user_id integer not null,
    job_id integer not null,
    date_applied date not null default current_date,

    primary key(caregiver_user_id, job_id), 

    constraint job_application_caregiver_const
    foreign key (caregiver_user_id)
    references caregiver(caregiver_user_id)
    on delete cascade, 

    constraint job_application_job_const
    foreign key (job_id)
    references job(job_id)
    on delete cascade
);

create table appointment(
    appointment_id serial primary key,
    caregiver_user_id integer not null,
    member_user_id integer not null,
    appointment_date date not null,
    appointment_time time not null,
    work_hours integer not null check (work_hours > 0), 
    status varchar(20) not null check (status in ('pending', 'accepted', 'declined')),

    constraint appoinment_caregiver_const
    foreign key (caregiver_user_id)
    references caregiver (caregiver_user_id)
    on delete cascade,

    constraint appointment_member_constraint 
    foreign key (member_user_id)
    references member(member_user_id)
    on delete cascade
);
