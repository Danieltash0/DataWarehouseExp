CREATE TABLE dim_student (
    student_id  INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    sex         CHAR(1) CHECK (sex IN ('M', 'F')),
    age         INT CHECK (age BETWEEN 15 AND 22),
    address     CHAR(1) CHECK (address IN ('U', 'R')),
    guardian    VARCHAR(20),
    romantic    BOOLEAN
);


CREATE TABLE dim_family (
    family_id   INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    famsize     VARCHAR(4) CHECK (famsize IN ('LE3', 'GT3')),
    pstatus     CHAR(1) CHECK (pstatus IN ('T', 'A')),
    medu        INT CHECK (medu BETWEEN 0 AND 4),
    fedu        INT CHECK (fedu BETWEEN 0 AND 4),
    mjob        VARCHAR(30),
    fjob        VARCHAR(30),
    famrel     INT CHECK (famrel BETWEEN 1 AND 5),
    famsup     BOOLEAN
);


CREATE TABLE dim_school (
    school_id   INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    school_code CHAR(2) CHECK (school_code IN ('GP', 'MS')),
    reason      VARCHAR(30),
    schoolsup   BOOLEAN,
    paid        BOOLEAN,
    activities  BOOLEAN,
    nursery     BOOLEAN,
    higher      BOOLEAN,
    internet    BOOLEAN
);


CREATE TABLE dim_subject (
    subject_id      INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    subject_name    VARCHAR(50) NOT NULL UNIQUE
);


CREATE TABLE fact_student_performance (
    performance_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    -- Foreign Keys
    student_id INT NOT NULL,
    family_id  INT NOT NULL,
    school_id  INT NOT NULL,
    subject_id INT NOT NULL,

    -- Academic & behavioral measures
    traveltime INT CHECK (traveltime BETWEEN 1 AND 4),
    studytime  INT CHECK (studytime BETWEEN 1 AND 4),
    failures   INT CHECK (failures BETWEEN 0 AND 4),

    freetime   INT CHECK (freetime BETWEEN 1 AND 5),
    goout      INT CHECK (goout BETWEEN 1 AND 5),

    dalc       INT CHECK (dalc BETWEEN 1 AND 5),
    walc       INT CHECK (walc BETWEEN 1 AND 5),
    health     INT CHECK (health BETWEEN 1 AND 5),

    absences   INT CHECK (absences BETWEEN 0 AND 93),

    g1         INT CHECK (g1 BETWEEN 0 AND 20),
    g2         INT CHECK (g2 BETWEEN 0 AND 20),
    g3         INT CHECK (g3 BETWEEN 0 AND 20),

    -- Constraints
    CONSTRAINT fk_student
        FOREIGN KEY (student_id) REFERENCES dim_student(student_id),

    CONSTRAINT fk_family
        FOREIGN KEY (family_id) REFERENCES dim_family(family_id),

    CONSTRAINT fk_school
        FOREIGN KEY (school_id) REFERENCES dim_school(school_id),

    CONSTRAINT fk_subject
        FOREIGN KEY (subject_id) REFERENCES dim_subject(subject_id),

    CONSTRAINT uq_student_subject UNIQUE (student_id, subject_id)
);

/*
ALTER TABLE
    `Fact_Student_Performance` ADD CONSTRAINT `fact_student_performance_school_id_foreign` FOREIGN KEY(`school_id`) REFERENCES `Dim_School`(`school_id`);
ALTER TABLE
    `Fact_Student_Performance` ADD CONSTRAINT `fact_student_performance_family_id_foreign` FOREIGN KEY(`family_id`) REFERENCES `Dim_Family`(`family_id`);
ALTER TABLE
    `Fact_Student_Performance` ADD CONSTRAINT `fact_student_performance_subject_id_foreign` FOREIGN KEY(`subject_id`) REFERENCES `Dim_Subject`(`subject_id`);
ALTER TABLE
    `Fact_Student_Performance` ADD CONSTRAINT `fact_student_performance_student_id_foreign` FOREIGN KEY(`student_id`) REFERENCES `Dim_Student`(`student_id`);
*/