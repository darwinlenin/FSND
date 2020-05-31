--
-- PostgreSQL database dump
--

-- Dumped from database version 12.2
-- Dumped by pg_dump version 12.2

-- Started on 2020-05-31 10:02:20

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE fyyur;
--
-- TOC entry 2857 (class 1262 OID 73921)
-- Name: fyyur; Type: DATABASE; Schema: -; Owner: fyuur
--

CREATE DATABASE fyyur WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'Spanish_Peru.1252' LC_CTYPE = 'Spanish_Peru.1252';


ALTER DATABASE fyyur OWNER TO fyuur;

\connect fyyur

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 204 (class 1259 OID 73929)
-- Name: Artist; Type: TABLE; Schema: public; Owner: fyuur
--

CREATE TABLE public."Artist" (
    id integer NOT NULL,
    name character varying,
    genres character varying(500),
    city character varying(120),
    state character varying(120),
    phone character varying(120),
    website character varying(120),
    facebook_link character varying(120),
    seeking_venue boolean NOT NULL,
    seeking_description character varying(120),
    image_link character varying(500),
    past_shows character varying,
    upcoming_shows character varying,
    past_shows_count integer NOT NULL,
    upcoming_shows_count integer NOT NULL
);


ALTER TABLE public."Artist" OWNER TO fyuur;

--
-- TOC entry 203 (class 1259 OID 73927)
-- Name: Artist_id_seq; Type: SEQUENCE; Schema: public; Owner: fyuur
--

CREATE SEQUENCE public."Artist_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Artist_id_seq" OWNER TO fyuur;

--
-- TOC entry 2858 (class 0 OID 0)
-- Dependencies: 203
-- Name: Artist_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: fyuur
--

ALTER SEQUENCE public."Artist_id_seq" OWNED BY public."Artist".id;


--
-- TOC entry 208 (class 1259 OID 73951)
-- Name: Show; Type: TABLE; Schema: public; Owner: fyuur
--

CREATE TABLE public."Show" (
    id integer NOT NULL,
    venue_id integer NOT NULL,
    venue_name character varying,
    artist_id integer NOT NULL,
    artist_name character varying,
    artist_image_link character varying(500),
    start_time timestamp with time zone
);


ALTER TABLE public."Show" OWNER TO fyuur;

--
-- TOC entry 207 (class 1259 OID 73949)
-- Name: Show_id_seq; Type: SEQUENCE; Schema: public; Owner: fyuur
--

CREATE SEQUENCE public."Show_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Show_id_seq" OWNER TO fyuur;

--
-- TOC entry 2859 (class 0 OID 0)
-- Dependencies: 207
-- Name: Show_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: fyuur
--

ALTER SEQUENCE public."Show_id_seq" OWNED BY public."Show".id;


--
-- TOC entry 206 (class 1259 OID 73940)
-- Name: Venue; Type: TABLE; Schema: public; Owner: fyuur
--

CREATE TABLE public."Venue" (
    id integer NOT NULL,
    name character varying,
    genres character varying(500),
    city character varying(120),
    state character varying(120),
    address character varying(120),
    phone character varying(120),
    website character varying(120),
    facebook_link character varying(120),
    seeking_talent boolean NOT NULL,
    seeking_description character varying(500),
    image_link character varying(500),
    past_shows character varying,
    upcoming_shows character varying,
    past_shows_count integer NOT NULL,
    upcoming_shows_count integer NOT NULL
);


ALTER TABLE public."Venue" OWNER TO fyuur;

--
-- TOC entry 205 (class 1259 OID 73938)
-- Name: Venue_id_seq; Type: SEQUENCE; Schema: public; Owner: fyuur
--

CREATE SEQUENCE public."Venue_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Venue_id_seq" OWNER TO fyuur;

--
-- TOC entry 2860 (class 0 OID 0)
-- Dependencies: 205
-- Name: Venue_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: fyuur
--

ALTER SEQUENCE public."Venue_id_seq" OWNED BY public."Venue".id;


--
-- TOC entry 202 (class 1259 OID 73922)
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: fyuur
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO fyuur;

--
-- TOC entry 2706 (class 2604 OID 73932)
-- Name: Artist id; Type: DEFAULT; Schema: public; Owner: fyuur
--

ALTER TABLE ONLY public."Artist" ALTER COLUMN id SET DEFAULT nextval('public."Artist_id_seq"'::regclass);


--
-- TOC entry 2708 (class 2604 OID 73954)
-- Name: Show id; Type: DEFAULT; Schema: public; Owner: fyuur
--

ALTER TABLE ONLY public."Show" ALTER COLUMN id SET DEFAULT nextval('public."Show_id_seq"'::regclass);


--
-- TOC entry 2707 (class 2604 OID 73943)
-- Name: Venue id; Type: DEFAULT; Schema: public; Owner: fyuur
--

ALTER TABLE ONLY public."Venue" ALTER COLUMN id SET DEFAULT nextval('public."Venue_id_seq"'::regclass);


--
-- TOC entry 2847 (class 0 OID 73929)
-- Dependencies: 204
-- Data for Name: Artist; Type: TABLE DATA; Schema: public; Owner: fyuur
--



--
-- TOC entry 2851 (class 0 OID 73951)
-- Dependencies: 208
-- Data for Name: Show; Type: TABLE DATA; Schema: public; Owner: fyuur
--



--
-- TOC entry 2849 (class 0 OID 73940)
-- Dependencies: 206
-- Data for Name: Venue; Type: TABLE DATA; Schema: public; Owner: fyuur
--



--
-- TOC entry 2845 (class 0 OID 73922)
-- Dependencies: 202
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: fyuur
--

INSERT INTO public.alembic_version (version_num) VALUES ('65f498ff306b');


--
-- TOC entry 2861 (class 0 OID 0)
-- Dependencies: 203
-- Name: Artist_id_seq; Type: SEQUENCE SET; Schema: public; Owner: fyuur
--

SELECT pg_catalog.setval('public."Artist_id_seq"', 16, true);


--
-- TOC entry 2862 (class 0 OID 0)
-- Dependencies: 207
-- Name: Show_id_seq; Type: SEQUENCE SET; Schema: public; Owner: fyuur
--

SELECT pg_catalog.setval('public."Show_id_seq"', 2, true);


--
-- TOC entry 2863 (class 0 OID 0)
-- Dependencies: 205
-- Name: Venue_id_seq; Type: SEQUENCE SET; Schema: public; Owner: fyuur
--

SELECT pg_catalog.setval('public."Venue_id_seq"', 4, true);


--
-- TOC entry 2712 (class 2606 OID 73937)
-- Name: Artist Artist_pkey; Type: CONSTRAINT; Schema: public; Owner: fyuur
--

ALTER TABLE ONLY public."Artist"
    ADD CONSTRAINT "Artist_pkey" PRIMARY KEY (id);


--
-- TOC entry 2716 (class 2606 OID 73959)
-- Name: Show Show_pkey; Type: CONSTRAINT; Schema: public; Owner: fyuur
--

ALTER TABLE ONLY public."Show"
    ADD CONSTRAINT "Show_pkey" PRIMARY KEY (id);


--
-- TOC entry 2714 (class 2606 OID 73948)
-- Name: Venue Venue_pkey; Type: CONSTRAINT; Schema: public; Owner: fyuur
--

ALTER TABLE ONLY public."Venue"
    ADD CONSTRAINT "Venue_pkey" PRIMARY KEY (id);


--
-- TOC entry 2710 (class 2606 OID 73926)
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: fyuur
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- TOC entry 2717 (class 2606 OID 73960)
-- Name: Show Show_artist_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: fyuur
--

ALTER TABLE ONLY public."Show"
    ADD CONSTRAINT "Show_artist_id_fkey" FOREIGN KEY (artist_id) REFERENCES public."Artist"(id);


--
-- TOC entry 2718 (class 2606 OID 73965)
-- Name: Show Show_venue_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: fyuur
--

ALTER TABLE ONLY public."Show"
    ADD CONSTRAINT "Show_venue_id_fkey" FOREIGN KEY (venue_id) REFERENCES public."Venue"(id);


-- Completed on 2020-05-31 10:02:24

--
-- PostgreSQL database dump complete
--

