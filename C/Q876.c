#include<stdio.h>
#include<stdlib.h>
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
void middleNode(struct node* head) {
    struct node * p=head;int c=0,i=0;
    while(p!=NULL){c++;p=p->next;}
    c=1 + c/2;p=head;
    while(i<c){
        p=p->next;i++;
    }printf("%d",p->data);
    // head=p;return head;
}
void dlt(struct node*head,int data){
    struct node*p=head;
    while (p->data!=data&&p->next!=NULL){p=p->next;}printf("%d",p->data);
    // if (p->next=NULL){p->next=NULL;}
    p->next=p->next->next;
}

void main()
{
    struct node *head,*p;int n,g, m=1;
    head=(struct node*) malloc(sizeof(struct node));
    create(head,5);
    // middleNode(head);
    dlt(head,5);
    trv(head);

}