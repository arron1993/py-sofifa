
FROM node:lts-alpine as node
WORKDIR /app
COPY . .
RUN yarn install
RUN npx ng build --configuration production

FROM nginx:alpine

COPY ./nginx/default.conf /etc/nginx/conf.d/
COPY --from=node /app/dist/ng-attribute-collector /usr/share/nginx/html