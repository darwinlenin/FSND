INSERT INTO public."Venue"(
	id, name, city, state, address, phone, website, facebook_link, seeking_talent, 
	image_link, past_shows, upcoming_shows, past_shows_count, upcoming_shows_count, 
	seeking_description, genres)
	VALUES (1,'The Musical Hop',
'San Francisco',
'CA',
'1015 Folsom Street',
'123-123-1234',
'https://www.themusicalhop.com',
'https://www.facebook.com/TheMusicalHop',
True, 
'https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60', 
'[{
      "artist_id": 4,
      "artist_name": "Guns N Petals",
      "artist_image_link": "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80",
      "start_time": "2019-05-21T21:30:00.000Z"
    }]', '[]',1,0,
'We are on the lookout for a local artist to play every two weeks. Please call us.',
'["Jazz", "Reggae", "Swing", "Classical", "Folk"]');
	
	
INSERT INTO public."Venue"(
	id, name, city, state, address, phone, website, facebook_link, seeking_talent, 
	image_link,past_shows,upcoming_shows, past_shows_count, upcoming_shows_count, genres)
	VALUES (2,'The Dueling Pianos Bar',
'New York',
'NY',
'335 Delancey Street',
'914-003-1132',
'https://www.theduelingpianos.com',
'https://www.facebook.com/theduelingpianos',
False, 
'https://images.unsplash.com/photo-1497032205916-ac775f0649ae?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80', 
'[]','[]',0,0,
'["Classical", "R&B", "Hip-Hop"]');

INSERT INTO public."Venue"(
	id, name, city, genres, state, address, phone, website, facebook_link, 
	seeking_talent, 
	image_link, past_shows, upcoming_shows, past_shows_count, 
	upcoming_shows_count)
	VALUES (3,'Park Square Live Music & Coffee',
'San Francisco',
'["Rock n Roll", "Jazz", "Classical", "Folk"]',
'CA',
'34 Whiskey Moore Ave',
'415-000-1234',
'https://www.parksquarelivemusicandcoffee.com',
'https://www.facebook.com/ParkSquareLiveMusicAndCoffee',
False, 
'https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80', 
'[{
      "artist_id": 5,
      "artist_name": "Matt Quevedo",
      "artist_image_link": "https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80",
      "start_time": "2019-06-15T23:00:00.000Z"
    }]', '[{
      "artist_id": 6,
      "artist_name": "The Wild Sax Band",
      "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
      "start_time": "2035-04-01T20:00:00.000Z"
    }, {
      "artist_id": 6,
      "artist_name": "The Wild Sax Band",
      "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
      "start_time": "2035-04-08T20:00:00.000Z"
    }, {
      "artist_id": 6,
      "artist_name": "The Wild Sax Band",
      "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
      "start_time": "2035-04-15T20:00:00.000Z"
    }]',1,1);

INSERT INTO public."Genre"(
	name)
	VALUES ('Jazz');
INSERT INTO public."Genre"(
	name, venue_id)
	VALUES ('Reggae');
	
INSERT INTO public."Genre"(
	name, venue_id)
	VALUES ('Swing');
	
INSERT INTO public."Genre"(
	name, venue_id)
	VALUES ('Classical');
	
INSERT INTO public."Genre"(
	name, venue_id)
	VALUES ('Folk');
	

	
	
INSERT INTO public."Artist"(
	id, name, city, state, phone, website, facebook_link, seeking_venue, 
	image_link, past_shows, upcoming_shows, past_shows_count, upcoming_shows_count, 
	seeking_description, genres)
	VALUES (4,'Guns N Petals',
'San Francisco',
'CA',
'326-123-5000',
'https://www.gunsnpetalsband.com',
'https://www.facebook.com/GunsNPetals',
True, 
'https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80', 
'[{
      "venue_id": 1,
      "venue_name": "The Musical Hop",
      "venue_image_link": "https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60",
      "start_time": "2019-05-21T21:30:00.000Z"
    }]', '[]',1,0,
'Looking for shows to perform at in the San Francisco Bay Area!',
'["Rock n Roll"]');


INSERT INTO public."Artist"(
	id, name, city, state, phone, website, facebook_link, seeking_venue, 
	image_link,past_shows,upcoming_shows, past_shows_count, upcoming_shows_count, genres)
	VALUES (5,'Matt Quevedo',
'New York',
'NY',
'300-400-5000',
'https://www.theduelingpianos.com',
'https://www.facebook.com/mattquevedo923251523',
False, 
'https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80', 
'[{
      "venue_id": 3,
      "venue_name": "Park Square Live Music & Coffee",
      "venue_image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80",
      "start_time": "2019-06-15T23:00:00.000Z"
    }]','[]',1,0,
'["Jazz"]');


INSERT INTO public."Artist"(
	id, name, city, genres, state, phone, 
	seeking_venue, 
	image_link, past_shows, upcoming_shows, past_shows_count, 
	upcoming_shows_count)
	VALUES (6,'The Wild Sax Band',
'San Francisco',
'["Jazz", "Classical"]',
'CA',
'432-325-5432',
False, 
'https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80', 
'[]',
'[{
      "venue_id": 3,
      "venue_name": "Park Square Live Music & Coffee",
      "venue_image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80",
      "start_time": "2035-04-01T20:00:00.000Z"
    }, {
      "venue_id": 3,
      "venue_name": "Park Square Live Music & Coffee",
      "venue_image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80",
      "start_time": "2035-04-08T20:00:00.000Z"
    }, {
      "venue_id": 3,
      "venue_name": "Park Square Live Music & Coffee",
      "venue_image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80",
      "start_time": "2035-04-15T20:00:00.000Z"
    }]',0,3);
	
	
	
	
UPDATE public."Artist"
	SET genres='[]'
	WHERE id=1;
	
	