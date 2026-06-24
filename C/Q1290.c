#include<stdio.h>
#include<stdlib.h>
#include<math.h>
struct node {
     int data;
     struct node *next;
};
struct node * create(struct node *head,int n){
    struct node *p;p=head;
    for (int i=0;i<=n;i++){
    p->next=(struct node*) malloc(sizeof(struct node));p=p->next;
    //  printf("node %d: ",i+1);scanf("%d",&p->data);
    p->data=i+3;
            }p->next=NULL;return p;}
void trv(struct node *head){
    struct node *p=NULL;p=head;p=p->next;
    while (p!=NULL)
    {printf("%d -> ",p->data);p=p->next;}}
void Q(struct node*head){
    int i=0,k=0;

struct node*p=head;double a=0,c;
while(p!=NULL){k++;p=p->next;}p=head->next;
i=k;

    while (p!= NULL)
    {c=p->data;p=p->next;
    a=a+c*pow(2,i);i--;
    printf("%lf\n",a);
    }int b=a;
     printf("%d",b);
}

void main()
{
    struct node *head;
    head=(struct node*) malloc(sizeof(struct node));
struct node*p=head;
p->next=(struct node*) malloc(sizeof(struct node));p=p->next;p->data=1;
p->next=(struct node*) malloc(sizeof(struct node));p=p->next;p->data=0;
p->next=(struct node*) malloc(sizeof(struct node));p=p->next;p->data=1;
p->next=NULL;
    trv(head);
    // int b=
     Q(head);
        //  printf("%d",b);

}