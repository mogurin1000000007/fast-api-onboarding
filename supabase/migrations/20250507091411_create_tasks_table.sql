create table if not exists tasks (
    id uuid default gen_random_uuid() primary key,
    title text not null,
    done boolean default false,
    created_at timestamp with time zone default now(),
    updated_at timestamp with time zone default now()
);
